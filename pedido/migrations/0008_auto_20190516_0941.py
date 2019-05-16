# Generated by Django 2.1.7 on 2019-05-16 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0007_auto_20190515_1043'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pedido',
            old_name='carne',
            new_name='carne_opcao_1',
        ),
        migrations.AddField(
            model_name='pedido',
            name='carne_opcao_2',
            field=models.CharField(choices=[('Boi', 'Boi'), ('Frango', 'Frango'), ('Porco', 'Porco'), ('Picadinho', 'Picadinho')], max_length=50, null=True),
        ),
    ]
