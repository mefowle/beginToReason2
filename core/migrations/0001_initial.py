# Generated by Django 3.1.2 on 2021-02-06 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_name', models.CharField(max_length=30)),
                ('lesson_code', models.TextField(max_length=750)),
            ],
        ),
        migrations.CreateModel(
            name='Concept',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('concept_key', models.CharField(max_length=30)),
                ('concept_text', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(default='Try Again!', max_length=50)),
                ('feedback_type', models.CharField(choices=[('DEF', 'Default'), ('COR', 'Correct'), ('SIM', 'Simplify'), ('SELF', 'Self Reference'), ('NUM', 'Used Concrete Value as Answer'), ('INIT', 'Missing # Symbol'), ('ALG', 'Algebra'), ('VAR', 'Variable'), ('SUB', 'Sub_Lesson')], default='DEF', max_length=4)),
                ('feedback_text', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='IncorrectAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson_text', models.CharField(default='Lesson2', max_length=200)),
                ('answer_type', models.CharField(choices=[('SIM', 'Simplify'), ('SELF', 'Self Reference'), ('NUM', 'Used Concrete Value as Answer'), ('INIT', 'Missing # Symbol'), ('ALG', 'Algebra'), ('VAR', 'Variable')], default='SIM', max_length=4)),
                ('answer_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson_name', models.CharField(max_length=50)),
                ('lesson_title', models.CharField(default='default', max_length=50)),
                ('lesson_index', models.IntegerField(default=0)),
                ('instruction', models.TextField(default='Please complete the Confirm assertion(s) and check correctness.')),
                ('correct', models.CharField(default='Lesson To Go To', max_length=50)),
                ('correct_feedback', models.TextField(default='Proceeding to the next lesson.')),
                ('is_walkthrough', models.BooleanField(default=False)),
                ('is_alternate', models.BooleanField(default=False)),
                ('can_mutate', models.BooleanField(default=False)),
                ('sub_lessons_available', models.BooleanField(default=False)),
                ('simplify', models.CharField(default='None', max_length=50)),
                ('self_reference', models.CharField(default='None', max_length=50)),
                ('use_of_concrete_values', models.CharField(default='None', max_length=50)),
                ('not_using_initial_value', models.CharField(default='None', max_length=50)),
                ('algebra', models.CharField(default='None', max_length=50)),
                ('variable', models.CharField(default='None', max_length=50)),
                ('screen_record', models.BooleanField(default=False)),
                ('audio_record', models.BooleanField(default=False)),
                ('audio_transcribe', models.BooleanField(default=False)),
                ('code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.code')),
                ('feedback', models.ManyToManyField(blank=True, to='core.Feedback')),
                ('incorrect_answers', models.ManyToManyField(blank=True, to='core.IncorrectAnswer')),
                ('lesson_concept', models.ManyToManyField(blank=True, to='core.Concept')),
            ],
        ),
        migrations.CreateModel(
            name='LessonSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('set_name', models.CharField(max_length=50)),
                ('set_description', models.TextField(default='This set is designed to further your understanding')),
                ('set_image', models.ImageField(default='begin.png', upload_to=None)),
                ('first_in_set', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='first_in_set', to='core.lesson')),
                ('lessons', models.ManyToManyField(blank=True, to='core.Lesson')),
            ],
        ),
        migrations.CreateModel(
            name='McChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_key', models.CharField(max_length=30)),
                ('reference_text', models.TextField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Reasoning',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reasoning_name', models.CharField(max_length=30)),
                ('reasoning_type', models.CharField(choices=[('MC', 'Multiple Choice'), ('Text', 'Free Response'), ('Both', 'Multiple Choice and Free Response'), ('None', 'None')], default='None', max_length=4)),
                ('mc_set', models.ManyToManyField(blank=True, to='core.McChoice')),
                ('reasoning_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.question')),
            ],
        ),
        migrations.AddField(
            model_name='mcchoice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.question'),
        ),
        migrations.CreateModel(
            name='MainSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('set_name', models.CharField(max_length=50)),
                ('set_description', models.TextField(default='This set is designed to further your understanding')),
                ('lessons', models.ManyToManyField(blank=True, to='core.LessonSet')),
            ],
        ),
        migrations.AddField(
            model_name='lesson',
            name='reason',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.reasoning'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='reference_set',
            field=models.ManyToManyField(blank=True, to='core.Reference'),
        ),
    ]
