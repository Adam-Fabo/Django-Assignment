# Generated by Django 4.1 on 2022-08-30 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='AttributeName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazev', models.CharField(blank=True, max_length=100)),
                ('kod', models.CharField(blank=True, max_length=100)),
                ('zobrazit', models.BooleanField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AttributeValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hodnota', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obrazek', models.URLField(blank=True, max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazev', models.CharField(blank=True, max_length=100)),
                ('description', models.TextField(blank=True, max_length=1000)),
                ('cena', models.IntegerField()),
                ('mena', models.CharField(blank=True, max_length=20)),
                ('is_published', models.BooleanField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazev', models.CharField(blank=True, max_length=100)),
                ('obrazek_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='elements.image')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='elements.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductAttributes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='elements.attribute')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='elements.product')),
            ],
        ),
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazev', models.CharField(blank=True, max_length=100)),
                ('obrazek_id', models.IntegerField(blank=True, null=True)),
                ('attributes_ids', models.ManyToManyField(blank=True, to='elements.attribute')),
                ('products_ids', models.ManyToManyField(blank=True, to='elements.product')),
            ],
        ),
        migrations.AddField(
            model_name='attribute',
            name='hodnota_atributu_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='elements.attributevalue'),
        ),
        migrations.AddField(
            model_name='attribute',
            name='nazev_atributu_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='elements.attributename'),
        ),
    ]