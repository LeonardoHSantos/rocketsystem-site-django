# Generated by Django 4.2.4 on 2023-08-19 03:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_webhook', '0004_deals_person'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deals',
            old_name='current_active',
            new_name='current_deal_active',
        ),
        migrations.RenameField(
            model_name='deals',
            old_name='current_add_time',
            new_name='current_deal_add_time',
        ),
        migrations.RenameField(
            model_name='deals',
            old_name='current_id',
            new_name='current_deal_id',
        ),
        migrations.RenameField(
            model_name='deals',
            old_name='current_org_name',
            new_name='current_deal_org_name',
        ),
        migrations.RenameField(
            model_name='deals',
            old_name='current_owner_name',
            new_name='current_deal_owner_name',
        ),
        migrations.RenameField(
            model_name='deals',
            old_name='current_person_id',
            new_name='current_deal_person_id',
        ),
        migrations.RenameField(
            model_name='deals',
            old_name='current_person_name',
            new_name='current_deal_person_name',
        ),
        migrations.RenameField(
            model_name='deals',
            old_name='current_pipeline_id',
            new_name='current_deal_pipeline_id',
        ),
        migrations.RenameField(
            model_name='deals',
            old_name='current_stage_id',
            new_name='current_deal_stage_id',
        ),
        migrations.RenameField(
            model_name='deals',
            old_name='current_status',
            new_name='current_deal_status',
        ),
        migrations.RenameField(
            model_name='deals',
            old_name='current_title',
            new_name='current_deal_title',
        ),
        migrations.RenameField(
            model_name='deals',
            old_name='current_update_time',
            new_name='current_deal_update_time',
        ),
        migrations.RenameField(
            model_name='deals',
            old_name='current_value',
            new_name='current_deal_value',
        ),
        migrations.RenameField(
            model_name='deals',
            old_name='current_weighted_value',
            new_name='current_deal_weighted_value',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='current_add_time',
            new_name='current_person_add_time',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='current_email',
            new_name='current_person_email',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='current_id',
            new_name='current_person_id',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='current_name',
            new_name='current_person_name',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='current_open_deals_count',
            new_name='current_person_open_deals_count',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='current_owner_name',
            new_name='current_person_owner_name',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='current_phone',
            new_name='current_person_phone',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='current_update_time',
            new_name='current_person_update_time',
        ),
    ]
