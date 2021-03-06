from django.core.management.base import BaseCommand
from myapp.models import User,Activity_Periods
from sampledatahelper.helper import SampleDataHelper

class Command(BaseCommand):
    args = ''
    help = 'Example data generator'
    sd = SampleDataHelper(seed=12345678901)

    def generate_mymodel_data(self, instances):
        choices = ["America/Los_Angeles","Belgium/Brussels","Cambodia/Phnom Penh","Denmark/Copenhagen","Fiji/Suva","India/Kolkata","India/Ranchi","China/Wuhan","Russia/Moscow"]

        user_instance=User()
        for x in range(1,instances):
            instance = User.objects.create(
               uid=self.sd.hex_chars(min_chars=9, max_chars=9),
                real_name=self.sd.fullname(locale=None, as_list=False),
                tz=self.sd.choice(choices),
                
            )

        for outer_loop in range(1,instances):
            for inner_loop in range(3):
                activeity_period = Activity_Periods.objects.create(
                    start_time=self.sd.datetime(begin=-1440, end=1440),
                    end_time=self.sd.datetime(begin=-1440, end=1440),
                    user = User.objects.get(id=outer_loop)
                    
                )

    def handle(self, *args, **options):
        print("Generating MyModel data")
        self.generate_mymodel_data(51)