# Generated by Django 5.0.8 on 2024-08-14 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_testemunho_estrelas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testemunho',
            name='estrelas',
            field=models.CharField(choices=[('★☆☆☆☆', '1 estrela'), ('★★☆☆☆', '2 estrelas'), ('★★★☆☆', '3 estrelas'), ('★★★★☆', '4 estrelas'), ('★★★★★', '5 estrelas')], max_length=100, verbose_name='Estrelas'),
        ),
    ]
