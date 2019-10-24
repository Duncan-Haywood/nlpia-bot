# Generated by Django 2.2.4 on 2019-09-26 02:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0004_auto_20190926_0205'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('context_name', models.TextField()),
                ('agent', models.TextField(help_text='Human or bot agent expected to take the next turn or action')),
            ],
        ),
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('probability', models.FloatField(blank=True, default=1, null=True)),
                ('action_name', models.TextField(default='text')),
                ('payload', models.TextField(blank=True, default='', help_text="parameters of the action, in the case of the aciton 'text' or 'say', just the string to be uttered", null=True)),
                ('agent', models.ForeignKey(help_text='The human or autonomous agent that can perform this action', on_delete=django.db.models.deletion.PROTECT, to='bot.Agent')),
                ('dest', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='dest', to='bot.State')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='source', to='bot.State')),
            ],
        ),
    ]