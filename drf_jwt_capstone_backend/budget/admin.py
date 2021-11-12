from django.contrib import admin
from .models import Food
from .models import Personal_Expenses
from .models import Insurance
from .models import Transportation
from .models import Housing
from .models import Utilities


# Register your models here.

admin.site.register(Food)
admin.site.register(Personal_Expenses)
admin.site.register(Insurance)
admin.site.register(Transportation)
admin.site.register(Housing)
admin.site.register(Utilities)