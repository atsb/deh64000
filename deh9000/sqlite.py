"""Interface module that exposes a DehackedFile as SQLite tables.

This uses the SQLite "virtual table" functionality to make the tables
associated with a given DehackedFile object accessible via SQL. The table
contents can be queried and modified via SQL.

Based on the apsw (Another Python SQLite Wrapper) library; also included
is a subclass of the apsw.Shell class that implements DEH9000-related
subcommands to load and save Dehacked files.
"""

from __future__ import absolute_import
from __future__ import print_function

import unittest

import apsw

from deh9000 import actions
from deh9000 import c
from deh9000 import strings
from deh9000.ammo import ammotype_t
from deh9000.file import DehackedFile
from deh9000.mobjs import mobjtype_t
from deh9000.states import state_t, S_PISTOL
from deh9000.states import statenum_t
from deh9000.weapons import weapontype_t

TABLES = {
    "ammodata": ammotype_t,
    "miscdata": None,
    "mobjinfo": mobjtype_t,
    "states": statenum_t,
    "weaponinfo": weapontype_t,
}


class Cursor(object):
    """Implements the apsw.VTCursor interface.

	This allows values to be read from out of a c.StructArray into
	SQLite.
	"""

    def __init__(self, table):
        self.position = 0
        self.table = table

    def Close(self):
        pass

    def Column(self, number):
        return self.table[number, self.position]

    def Eof(self):
        return self.position >= len(self.table)

    def Filter(self, indexnum, indexname, constraintargs):
        pass

    def Next(self):
        self.position += 1

    def Rowid(self):
        return self.position


class Table(object):
    """Implementation of the apsw.VTTable interface.

	This wraps a c.StructArray object as a virtual table that can be
	queried and modified.
	"""
    METADATA_COLUMNS = [
        "id",
        "enum_name",
        "object_name",
    ]
    COLUMN_ROWID = 0
    COLUMN_ENUM_NAME = 1
    COLUMN_OBJECT_NAME = 2

    def __init__(self, struct_array, enum_type):
        self.struct_array = struct_array
        self.enum_type = enum_type
        self.data_columns = type(struct_array[0]).field_names()

    def column_names(self):
        return Table.METADATA_COLUMNS + self.data_columns

    def BestIndex(self, constraints, orderbys):
        pass

    def Open(self):
        return Cursor(self)

    def Disconnect(self):
        pass

    Destroy = Disconnect

    def __len__(self):
        return len(self.struct_array)

    def _metadata_cell(self, row, column):
        if column == Table.COLUMN_ROWID:
            return row
        elif column == Table.COLUMN_ENUM_NAME and self.enum_type:
            return self.enum_type[row]
        elif column == Table.COLUMN_OBJECT_NAME:
            return self.struct_array[row].object_name

    def __getitem__(self, key):
        (column, row) = key
        if column == -1:
            return row
        if column < len(Table.METADATA_COLUMNS):
            return self._metadata_cell(row, column)
        data_column = column - len(Table.METADATA_COLUMNS)
        colname = self.data_columns[data_column]
        result = getattr(self.struct_array[row], colname)
        return self._convert_to_sql_value(result)

    def _convert_to_sql_value(self, value):
        # We represent action pointers by their string name:
        if isinstance(value, actions.Action):
            return value.name
        return value

    def _convert_from_sql_value(self, field, value):
        if field == state_t.action:
            if value == None:
                return None
            if not hasattr(actions, value):
                raise NameError("Unknown action pointer %r" % (
                    value))
            return getattr(actions, value)

        return value

    def _set_metadata_cell(self, row, column, value):
        if column == Table.COLUMN_OBJECT_NAME:
            self.struct_array[row].object_name = value
        else:
            raise IndexError("Cannot change field %r" % (
                Table.METADATA_COLUMNS[column]))

    def __setitem__(self, key, value):
        (column, row) = key
        if column < len(Table.METADATA_COLUMNS):
            return self._set_metadata_cell(row, column, value)
        data_column = column - len(Table.METADATA_COLUMNS)
        colname = self.data_columns[data_column]
        obj = self.struct_array[row]
        field = getattr(type(obj), colname)
        value = self._convert_from_sql_value(field, value)
        setattr(obj, colname, value)

    def UpdateChangeRow(self, rowid, newrowid, fields):
        for column, value in enumerate(fields):
            if self[column, rowid] != value:
                self[column, rowid] = value

    def UpdateDeleteRow(self, rowid):
        raise NotImplementedError()

    def UpdateInsertRow(self, rowid, fields):
        raise NotImplementedError()


class StringsTable(object):
    """Implementation of the apsw.VTTable interface.

	This wraps a deh9000 StringReplacements object producing a table that
	can be used to query and modify it.
	"""
    COLUMN_NAME = 0
    COLUMN_KEY = 1
    COLUMN_VALUE = 2

    def __init__(self, string_repls):
        self.string_repls = string_repls
        self._populate_table(strings)

    def _populate_table(self, mod):
        """Add all symbolic named strings from imported module.

		Module in this case is the deh9000.strings module.
		"""
        self.table_entries = []
        used_keys = set()
        for name in sorted(dir(mod)):
            if name.startswith("__"):
                continue
            key = getattr(mod, name)
            if not isinstance(key, str):
                continue
            self.table_entries.append((name, key))
            used_keys.add(key)

        # Add unnamed entries:
        for key, value in self.string_repls.items():
            if key not in used_keys:
                self.table_entries.append(('', key))

    def column_names(self):
        return ["name", "key", "value"]

    def BestIndex(self, constraints, orderbys):
        pass

    def Open(self):
        return Cursor(self)

    def Disconnect(self):
        pass

    Destroy = Disconnect

    def __len__(self):
        return len(self.table_entries)

    def __getitem__(self, key):
        (column, row) = key
        if column == -1:
            return row
        elif column == StringsTable.COLUMN_VALUE:
            x = self.table_entries[row][StringsTable.COLUMN_KEY]
            return self.string_repls[x]
        else:
            return self.table_entries[row][column]

    def __setitem__(self, key, value):
        (column, row) = key
        if column == StringsTable.COLUMN_VALUE:
            x = self.table_entries[row][StringsTable.COLUMN_KEY]
            self.string_repls[x] = value
        else:
            raise IndexError('cannot change name or key fields')

    def UpdateChangeRow(self, rowid, newrowid, fields):
        for column, value in enumerate(fields):
            if self[column, rowid] != value:
                self[column, rowid] = value

    def UpdateDeleteRow(self, rowid):
        # TODO
        raise NotImplementedError()

    def UpdateInsertRow(self, rowid, fields):
        name, key, value = fields
        if rowid is not None:
            raise ValueError("expecting no existing row")
        if key in self.string_repls:
            raise KeyError("row for key %r already present" % (
                key,))
        if name:
            raise ValueError(
                "name must be empty when inserting new row")
        result = len(self.table_entries)
        self.string_repls[key] = value
        self.table_entries.append((name, key))
        return result


class Module(object):
    """Implementation of the apsw.VTModule interface.

	This implements the module invoked by SQLite when virtual tables are
	instantiated.
	"""

    def __init__(self, dehfile):
        self.dehfile = dehfile

    def Create(self, connection, modulename,
               databasename, tablename, *args):
        if len(args) > 0:
            raise ValueError("no arguments permitted")
        if tablename not in TABLES:
            raise ValueError("valid tables: %s" % (
                "; ".join(TABLES.keys())))
        array = getattr(self.dehfile, tablename)
        # Hack for miscdata
        if isinstance(array, c.Struct):
            array = c.StructArray(type(array), [array])
        if tablename == "strings":
            table = StringsTable(array)
        else:
            table = Table(array, TABLES[tablename])

        create_sql = "CREATE TABLE %s (%s);" % (
            tablename, ", ".join(table.column_names()),
        )
        return create_sql, table

    Connect = Create


class Shell(apsw.Shell):
    """Extension of apsw.Shell with commands to read/write .deh files."""

    def __init__(self, dehfile, *args, **kwargs):
        self.dehfile = dehfile
        super().__init__(*args, **kwargs)

    def command_dehload(self, cmd):
        """dehload FILE: Load Dehacked patch from FILE."""
        self.dehfile.load(cmd[0])

    def command_dehsave(self, cmd):
        """dehsave FILE: Write Dehacked patch to FILE."""
        self.dehfile.save(cmd[0])

    def command_doom(self, cmd):
        """doom ARGS: Start an interactive session to test changes."""
        self.dehfile.interactive(cmd)


def MakeTables(dehfile, connection=None):
    """Create Dehacked virtual tables on the given SQLite connection.

	Args:
	  dehfile: instance of deh9000.dehfile to query.
	  connection: instance of apsw.Connection; if None then an in-memory
	      connection is created.
	Returns:
	  instance of apsw.Connection on which the tables were created.
	"""
    if not connection:
        connection = apsw.Connection(":memory:")
    mod = Module(dehfile)
    connection.createmodule("deh9000", mod)
    cursor = connection.cursor()
    for table in TABLES:
        cursor.execute("CREATE VIRTUAL TABLE %s USING deh9000()" % (
            table))
    return connection


class TestSqlite(unittest.TestCase):

    def setUp(self):
        self.dehfile = DehackedFile()
        self.conn = MakeTables(self.dehfile)

    def expected_table_rows(self, table_name):
        if table_name == "miscdata":
            return 1
        arr = getattr(self.dehfile, table_name)
        return len(arr)

    def test_query_all_tables(self):
        for t in TABLES:
            cursor = self.conn.cursor()
            rowcount = 0
            for row in cursor.execute("SELECT * FROM %s" % t):
                rowcount += 1
            self.assertEqual(rowcount, self.expected_table_rows(t))

    def test_update_query(self):
        cursor = self.conn.cursor()
        query = "SELECT tics FROM states WHERE rowid=%d" % S_PISTOL
        self.assertEqual(self.dehfile.states[S_PISTOL].tics, 1)
        for row in cursor.execute(query):
            self.assertEqual(row[0], 1)
        cursor.execute("""
			UPDATE states SET tics=tics*2
			WHERE rowid=%d
		""" % S_PISTOL)
        self.assertEqual(self.dehfile.states[S_PISTOL].tics, 2)
        for row in cursor.execute(query):
            self.assertEqual(row[0], 2)

    def test_action_pointer_conversion(self):
        cursor = self.conn.cursor()
        query = "SELECT action FROM states WHERE rowid=%d" % S_PISTOL
        self.assertEqual(self.dehfile.states[S_PISTOL].action,
                         actions.A_WeaponReady)
        for row in cursor.execute(query):
            self.assertEqual(row[0], "A_WeaponReady")

        cursor.execute("""
			UPDATE states SET action='A_SkelFist'
			WHERE rowid=%d
		""" % S_PISTOL)
        self.assertEqual(self.dehfile.states[S_PISTOL].action,
                         actions.A_SkelFist)
        for row in cursor.execute(query):
            self.assertEqual(row[0], "A_SkelFist")

        cursor.execute("""
			UPDATE states SET action=NULL
			WHERE rowid=%d
		""" % S_PISTOL)
        self.assertEqual(self.dehfile.states[S_PISTOL].action, None)
        for row in cursor.execute(query):
            self.assertEqual(row[0], None)

    def test_metadata_fields(self):
        cursor = self.conn.cursor()
        query = """
			SELECT id, enum_name, object_name
			FROM mobjinfo
			WHERE rowid=0
		"""
        rows = list(cursor.execute(query))
        self.assertEqual(rows, [(0, "MT_PLAYER", "Player")])

        # object_name can be changed, other metadata fields can't:
        cursor.execute("""
			UPDATE mobjinfo SET object_name="Doomguy"
			WHERE rowid=0
		""")
        self.assertEqual(self.dehfile.mobjinfo[0].object_name,
                         "Doomguy")

        with self.assertRaises(IndexError):
            cursor.execute("""
				UPDATE mobjinfo SET id=1231424
				WHERE rowid=0
			""")
        with self.assertRaises(IndexError):
            cursor.execute("""
				UPDATE mobjinfo SET enum_name="asgkhjalsgk"
				WHERE rowid=0
			""")

    def test_strings_query(self):
        strings = self.dehfile.strings
        cursor = self.conn.cursor()
        rows = list(cursor.execute("""
			SELECT value FROM strings
			WHERE key="E1M2: Nuclear Plant"
		"""))
        self.assertEqual(rows, [("E1M2: Nuclear Plant",)])
        strings.HUSTR_E1M2 = "E1M2: Qux Refinery"
        rows = list(cursor.execute("""
			SELECT value FROM strings
			WHERE key="E1M2: Nuclear Plant"
		"""))
        self.assertEqual(rows, [("E1M2: Qux Refinery",)])

    def test_strings_update(self):
        strings = self.dehfile.strings
        cursor = self.conn.cursor()
        cursor.execute("""
			UPDATE strings SET value="E1M1: Foobar"
			WHERE name="HUSTR_E1M1"
		""")
        self.assertEqual(strings.HUSTR_E1M1, "E1M1: Foobar")

        with self.assertRaises(IndexError):
            cursor.execute("""
				UPDATE strings SET name="asfasf"
				WHERE rowid=0
			""")
        with self.assertRaises(IndexError):
            cursor.execute("""
				UPDATE strings SET key="asfasf"
				WHERE rowid=0
			""")

    def test_strings_insert(self):
        strings = self.dehfile.strings
        cursor = self.conn.cursor()
        cursor.execute("""
			INSERT INTO strings VALUES('', 'foo', 'bar')
		""")
        self.assertEqual(strings["foo"], "bar")

        # Can't conflict with existing row
        with self.assertRaises(KeyError):
            cursor.execute("""
				INSERT INTO strings
				VALUES('', 'E1M2: Nuclear Plant', 'x')
			""")
        # Can't specify a name:
        with self.assertRaises(ValueError):
            cursor.execute("""
				INSERT INTO strings VALUES('x', 'y', 'z')
			""")


if __name__ == "__main__":
    unittest.main()
