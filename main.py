from migration.migrate_to_db import migrate_to_db
from templates.family_template import family_record_template

# obj = migrate_to_db()
# obj.persistToDb()

obj = family_record_template()
obj.get_record(1)