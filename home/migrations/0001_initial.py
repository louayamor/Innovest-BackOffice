# Generated by Django 5.0.5 on 2024-05-07 11:28

import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('revenue', models.DecimalField(decimal_places=0, max_digits=10)),
                ('profit', models.DecimalField(decimal_places=0, max_digits=10)),
                ('sector', models.CharField(max_length=255)),
                ('country', models.CharField(blank=True, max_length=255, null=True)),
                ('image_blob', models.BinaryField(blank=True, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sector_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Investment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=3, max_digits=10)),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='investments', to='home.business')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, validators=[django.core.validators.EmailValidator()], verbose_name='email address')),
                ('roles', models.CharField(choices=[('ROLE_USER', 'ROLE_USER'), ('ROLE_ADMIN', 'ROLE_ADMIN')], max_length=50)),
                ('is_active', models.BooleanField(default=True)),
                ('username', models.CharField(max_length=255)),
                ('is_verified', models.BooleanField(default=False)),
                ('is_investor', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('all_investments', models.ManyToManyField(related_name='investors', to='home.investment')),
                ('businesses', models.ManyToManyField(related_name='owners', to='home.business')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='investment',
            name='investor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='investments', to='home.user'),
        ),
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_conversations', to='home.user')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_conversations', to='home.user')),
            ],
        ),
        migrations.AddField(
            model_name='business',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owned_businesses', to='home.user'),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('age', models.IntegerField(null=True)),
                ('country', models.CharField(max_length=255, null=True)),
                ('profile_image', models.BinaryField(null=True)),
                ('bio', models.TextField(null=True)),
                ('phone_number', models.IntegerField(null=True)),
                ('gender', models.CharField(max_length=255, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='home.user')),
            ],
        ),
    ]
