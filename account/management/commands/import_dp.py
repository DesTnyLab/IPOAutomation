import csv
from django.core.management.base import BaseCommand
from account.models import DpIdReverse


class Command(BaseCommand):
    help = "Import bulk DpIdReverse data from a CSV file"

    def add_arguments(self, parser):
        parser.add_argument("file_path", type=str, help="Path to the CSV file")

    def handle(self, *args, **kwargs):
        file_path = kwargs["file_path"]

        try:
            with open(file_path, mode="r", encoding="utf-8") as csvfile:
                reader = csv.DictReader(csvfile)
                count = 0

                for row in reader:
                    dp_id = row.get("dp_id")
                    clientId = row.get("clientId")
                    name = row.get("name")

                    if dp_id and clientId:
                        obj, created = DpIdReverse.objects.get_or_create(
                            dp_id=dp_id,
                            defaults={"clientId": clientId, "name": name}
                        )
                        if not created:
                            obj.clientId = clientId  # update if exists
                            obj.name = name
                            obj.save()
                        count += 1

                self.stdout.write(self.style.SUCCESS(f"Successfully imported {count} records."))

        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Error: {str(e)}"))
