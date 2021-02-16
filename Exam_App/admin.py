from django.contrib import admin
from .models import Users,Finalresults,Aptitude,Technical,Listquestions,Check_Select,quizattempt,quizattempt1,quizattempt2,Category,Aptitude1,Technical1,Aptitude2,Technical2

# Register your models here.
admin.site.register(Users)
admin.site.register(Aptitude)
admin.site.register(Technical)
admin.site.register(Check_Select)
admin.site.register(Listquestions)
admin.site.register(quizattempt)
admin.site.register(quizattempt1)
admin.site.register(quizattempt2)
admin.site.register(Finalresults)
admin.site.register(Category)
admin.site.register(Aptitude1)
admin.site.register(Technical1)
admin.site.register(Aptitude2)
admin.site.register(Technical2)
