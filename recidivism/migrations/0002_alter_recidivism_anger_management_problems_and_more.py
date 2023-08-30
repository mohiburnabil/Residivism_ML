# Generated by Django 4.2.2 on 2023-06-09 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recidivism', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recidivism',
            name='Anger_management_problems',
            field=models.IntegerField(choices=[(1, 'low'), (2, 'medium'), (3, 'high')]),
        ),
        migrations.AlterField(
            model_name='recidivism',
            name='Attention_deficit_or_hyperactivity_difficulties',
            field=models.IntegerField(choices=[(1, 'low'), (2, 'medium'), (3, 'high')]),
        ),
        migrations.AlterField(
            model_name='recidivism',
            name='Childhood_history_of_maltreatment',
            field=models.IntegerField(choices=[(1, 'low'), (2, 'medium'), (3, 'high')]),
        ),
        migrations.AlterField(
            model_name='recidivism',
            name='Community_disorganization',
            field=models.IntegerField(choices=[(1, 'low'), (2, 'medium'), (3, 'high')]),
        ),
        migrations.AlterField(
            model_name='recidivism',
            name='Early_caregiver_disruption',
            field=models.IntegerField(choices=[(1, 'low'), (2, 'medium'), (3, 'high')]),
        ),
        migrations.AlterField(
            model_name='recidivism',
            name='Early_initiation_of_violence',
            field=models.IntegerField(choices=[(1, 'low'), (2, 'medium'), (3, 'high')]),
        ),
        migrations.AlterField(
            model_name='recidivism',
            name='Exposure_to_violence_in_the_home',
            field=models.IntegerField(choices=[(1, 'low'), (2, 'medium'), (3, 'high')]),
        ),
        migrations.AlterField(
            model_name='recidivism',
            name='History_of_non_violent_offending',
            field=models.IntegerField(choices=[(1, 'low'), (2, 'medium'), (3, 'high')]),
        ),
        migrations.AlterField(
            model_name='recidivism',
            name='History_of_self_harm_or_suicide_attempts',
            field=models.IntegerField(choices=[(1, 'low'), (2, 'medium'), (3, 'high')]),
        ),
        migrations.AlterField(
            model_name='recidivism',
            name='History_of_violence',
            field=models.IntegerField(choices=[(1, 'low'), (2, 'medium'), (3, 'high')]),
        ),
        migrations.AlterField(
            model_name='recidivism',
            name='Lack_of_personal_or_social_support',
            field=models.IntegerField(choices=[(1, 'low'), (2, 'medium'), (3, 'high')]),
        ),
        migrations.AlterField(
            model_name='recidivism',
            name='Low_interest_or_Commitment_or_to_school',
            field=models.IntegerField(choices=[(1, 'low'), (2, 'medium'), (3, 'high')]),
        ),
        migrations.AlterField(
            model_name='recidivism',
            name='Negative_attitudes',
            field=models.IntegerField(choices=[(1, 'low'), (2, 'medium'), (3, 'high')]),
        ),
        migrations.AlterField(
            model_name='recidivism',
            name='Parental_or_caregiver_criminality',
            field=models.IntegerField(choices=[(1, 'low'), (2, 'medium'), (3, 'high')]),
        ),
        migrations.AlterField(
            model_name='recidivism',
            name='Past_supervision',
            field=models.IntegerField(choices=[(1, 'low'), (2, 'medium'), (3, 'high')]),
        ),
        migrations.AlterField(
            model_name='recidivism',
            name='Peer_delinquency',
            field=models.IntegerField(choices=[(1, 'low'), (2, 'medium'), (3, 'high')]),
        ),
        migrations.AlterField(
            model_name='recidivism',
            name='Peer_rejection',
            field=models.IntegerField(choices=[(1, 'low'), (2, 'medium'), (3, 'high')]),
        ),
        migrations.AlterField(
            model_name='recidivism',
            name='Poor_compliance',
            field=models.IntegerField(choices=[(1, 'low'), (2, 'medium'), (3, 'high')]),
        ),
        migrations.AlterField(
            model_name='recidivism',
            name='Poor_parental_management',
            field=models.IntegerField(choices=[(1, 'low'), (2, 'medium'), (3, 'high')]),
        ),
        migrations.AlterField(
            model_name='recidivism',
            name='Poor_school_achievement',
            field=models.IntegerField(choices=[(1, 'low'), (2, 'medium'), (3, 'high')]),
        ),
        migrations.AlterField(
            model_name='recidivism',
            name='Positive_attitude_toward_intervention_and_authority',
            field=models.IntegerField(choices=[(1, 'absent'), (2, 'present')]),
        ),
        migrations.AlterField(
            model_name='recidivism',
            name='Prosocial_involvement',
            field=models.IntegerField(choices=[(1, 'absent'), (2, 'present')]),
        ),
        migrations.AlterField(
            model_name='recidivism',
            name='Psychopathic_traits',
            field=models.IntegerField(choices=[(1, 'low'), (2, 'medium'), (3, 'high')]),
        ),
        migrations.AlterField(
            model_name='recidivism',
            name='Resilient_personality_traits',
            field=models.IntegerField(choices=[(1, 'absent'), (2, 'present')]),
        ),
        migrations.AlterField(
            model_name='recidivism',
            name='Risk_taking_or_Impulsivity',
            field=models.IntegerField(choices=[(1, 'low'), (2, 'medium'), (3, 'high')]),
        ),
        migrations.AlterField(
            model_name='recidivism',
            name='Stress_and_poor_coping',
            field=models.IntegerField(choices=[(1, 'low'), (2, 'medium'), (3, 'high')]),
        ),
        migrations.AlterField(
            model_name='recidivism',
            name='Strong_attachment_and_bonds',
            field=models.IntegerField(choices=[(1, 'absent'), (2, 'present')]),
        ),
        migrations.AlterField(
            model_name='recidivism',
            name='Strong_commitment_to_school',
            field=models.IntegerField(choices=[(1, 'absent'), (2, 'present')]),
        ),
        migrations.AlterField(
            model_name='recidivism',
            name='Strong_social_support',
            field=models.IntegerField(choices=[(1, 'absent'), (2, 'present')]),
        ),
        migrations.AlterField(
            model_name='recidivism',
            name='Substance_use_difficulties',
            field=models.IntegerField(choices=[(1, 'low'), (2, 'medium'), (3, 'high')]),
        ),
        migrations.AlterField(
            model_name='recidivism',
            name='monthly_family_income',
            field=models.IntegerField(choices=[(1, 'no income'), (2, 'less than 1000 yuan'), (3, 'beteen 1000 to 1999 yuan'), (4, 'between 2000 to 3499'), (5, 'more than 3500')]),
        ),
    ]