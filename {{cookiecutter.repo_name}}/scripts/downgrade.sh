#!/bin/bash
docker-compose exec app alembic downgrade "-1"



# alembic downgrade -1
# This will run the downgrade() method of your latest revision and update the alembic_version table to indicate the revision you're now at.

# If you need to go back multiple migrations, run
#    alembic history
# to view a list of all the migrations in your project (from newest to oldest),
# then copy and paste the identifier of the migration you want to go back to:
#    alembic downgrade 8ac14e223d1e
