import logging
import time

from django.core.management import BaseCommand

from ASSOI_manage.management.commands.submodule.load_cadastral_data import CadastralLoader

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = """
           Init default data as: Default groups, users, permissions and cadastral data.
           """

    def handle(self, *args, **options):
        start = time.time()
        logger.info("Starting to upload cadastral data...")
        loader = CadastralLoader()
        loader.load()
        logger.info("...Cadastral data uploaded")
        end = time.time()
        logger.info(f"Default data init for {end - start} seconds")
