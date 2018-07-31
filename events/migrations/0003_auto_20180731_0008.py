# Generated by Django 2.0.5 on 2018-07-31 00:08

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_player_activation'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvitedUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('accepted', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='userevent',
            name='description',
            field=models.TextField(default='a'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userevent',
            name='occuring',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inviteduser',
            name='events',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.UserEvent'),
        ),
    ]
