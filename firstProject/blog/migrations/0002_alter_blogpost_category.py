# Generated by Django 3.2 on 2021-09-02 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='category',
            field=models.CharField(choices=[('国際情勢', 'Global'), ('国内情勢', 'Domestic'), ('その他', 'Other')], max_length=50, verbose_name='カテゴリ'),
        ),
    ]
