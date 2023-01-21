"""
Django command to wait for the database to be available
"""
import time
from typing import Any, Optional

from psycopg2 import OperationalError as Psycopg2Error

from django.core.management.base import BaseCommand
from django.db.utils import OperationalError


class Command(BaseCommand):
    """Django command to wair for database.

    Args:
        BaseCommand (_type_):Base Class to implement custom management commands
    """
    
    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        "Entrypoint for command."
        self.stdout.write("Waiting for database...")
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2Error, OperationalError):
                self.stdout.write("Databse unavailable, waiting 1 second...")
                time.sleep(1)
        
        self.stdout.write(self.style.SUCCESS("database available!"))