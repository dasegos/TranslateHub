# Generated by Django 5.2.2 on 2025-06-22 15:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('translations', '0003_alter_postcomment_answer_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postcomment',
            name='content_type',
            field=models.ForeignKey(limit_choices_to=models.Q(models.Q(('app_label', 'translations'), ('model', 'OriginalText')), models.Q(('app_label', 'translations'), ('model', 'Translation')), _connector='OR'), on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='contenttypes.contenttype', verbose_name='Model instance reference'),
        ),
    ]
