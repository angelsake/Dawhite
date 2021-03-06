# Generated by Django 2.2.14 on 2020-09-02 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20190630_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='additional_image1',
            field=models.ImageField(default='No Image', upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='additional_image2',
            field=models.ImageField(default='no Image', upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='additional_image3',
            field=models.ImageField(default='no Image', upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='additional_information',
            field=models.TextField(default='some text'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('S', 'Rolex'), ('RM', 'Richard Mille'), ('H', 'Hublot'), ('FM', 'Frank Muller'), ('AP', 'Audemars Piguet'), ('P', 'Patek Phillipe'), ('Z', 'Zenith'), ('B', 'Breitling'), ('C', 'Constantin'), ('O', 'Omega'), ('M', 'Montblanc'), ('V', 'Versace'), ('C', 'Cartier'), ('JL', 'Jaeger Lecoultre'), ('JC', 'Jacob and Co'), ('Co', 'Corum'), ('J', 'Jeweleries'), ('I', 'IWC')], max_length=2),
        ),
    ]
