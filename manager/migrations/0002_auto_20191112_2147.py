# Generated by Django 2.2.7 on 2019-11-12 21:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='championship_odds',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_date', models.DateTimeField()),
                ('game_quality', models.IntegerField()),
                ('opponent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='manager.Team')),
                ('team', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='manager.Team')),
            ],
        ),
    ]