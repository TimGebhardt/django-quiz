from models import Category, Quiz, QuizStatus, Answer, Question, Score
from django.contrib import admin

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

class QuizAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    radio_admin_fields = {'status': admin.VERTICAL}
    

admin.site.register(Category, CategoryAdmin)
admin.site.register(QuizStatus)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Answer)
admin.site.register(Question)
admin.site.register(Score)
