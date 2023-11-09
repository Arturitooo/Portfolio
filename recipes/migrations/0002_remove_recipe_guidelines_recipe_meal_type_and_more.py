# Generated by Django 4.2.1 on 2023-11-09 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='guidelines',
        ),
        migrations.AddField(
            model_name='recipe',
            name='meal_type',
            field=models.CharField(choices=[('Breafkfest', 'Breafkfest'), ('Brunch', 'Brunch'), ('Dinner', 'Dinner'), ('Supper', 'Supper')], default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recipe',
            name='cuisine',
            field=models.CharField(choices=[('🇵🇱', 'Polish'), ('🇩🇪', 'German'), ('🇮🇹Italian', 'Italian'), ('🇫🇷French', 'French'), ('🇺🇸American', 'American'), ('🇪🇸Spanish', 'Spanish'), ('🇯🇵Japanese', 'Japan'), ('🇮🇳Indian', 'Indian'), ('Other', 'Other')], max_length=50),
        ),
        migrations.CreateModel(
            name='Instruction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step_number', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=1500)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.recipe')),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('amount', models.CharField(max_length=50)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.recipe')),
            ],
        ),
    ]
