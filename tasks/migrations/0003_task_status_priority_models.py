import django.db.models.deletion
from django.db import migrations, models


STATUS_LABELS = {
    'not_started': 'Not Started',
    'ongoing': 'Ongoing',
    'completed': 'Completed',
    'missed': 'Missed',
}

PRIORITY_LABELS = {
    'low': 'Low',
    'medium': 'Medium',
    'high': 'High',
}


def migrate_task_values_to_models(apps, schema_editor):
    Task = apps.get_model('tasks', 'Task')
    TaskStatus = apps.get_model('tasks', 'TaskStatus')
    TaskPriority = apps.get_model('tasks', 'TaskPriority')

    statuses = {
        code: TaskStatus.objects.create(code = code, label = label)
        for code, label in STATUS_LABELS.items()
    }
    priorities = {
        code: TaskPriority.objects.create(code = code, label = label)
        for code, label in PRIORITY_LABELS.items()
    }

    for task in Task.objects.all().iterator():
        status_code = task.status_legacy
        priority_code = task.priority_legacy
        if status_code not in statuses:
            statuses[status_code] = TaskStatus.objects.create(
                code = status_code,
                label = status_code.replace('_', ' ').title(),
            )
        if priority_code not in priorities:
            priorities[priority_code] = TaskPriority.objects.create(
                code = priority_code,
                label = priority_code.replace('_', ' ').title(),
            )
        task.status_id = statuses[status_code].pk
        task.priority_id = priorities[priority_code].pk
        task.save(update_fields = ['status', 'priority'])


def restore_task_values(apps, schema_editor):
    Task = apps.get_model('tasks', 'Task')
    for task in Task.objects.iterator():
        task.status_legacy = task.status.code
        task.priority_legacy = task.priority.code
        task.save(update_fields = ['status_legacy', 'priority_legacy'])


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name = 'TaskPriority',
            fields = [
                ('id', models.BigAutoField(auto_created = True, primary_key = True, serialize = False, verbose_name = 'ID')),
                ('code', models.CharField(max_length = 20, unique = True)),
                ('label', models.CharField(max_length = 50)),
            ],
            options = {
                'ordering': ['label'],
                'verbose_name_plural': 'Task priorities',
            },
        ),
        migrations.CreateModel(
            name = 'TaskStatus',
            fields = [
                ('id', models.BigAutoField(auto_created = True, primary_key = True, serialize = False, verbose_name = 'ID')),
                ('code', models.CharField(max_length = 20, unique = True)),
                ('label', models.CharField(max_length = 50)),
            ],
            options = {
                'ordering': ['label'],
                'verbose_name_plural': 'Task statuses',
            },
        ),
        migrations.RenameField(
            model_name = 'task',
            old_name = 'status',
            new_name = 'status_legacy',
        ),
        migrations.RenameField(
            model_name = 'task',
            old_name = 'priority',
            new_name = 'priority_legacy',
        ),
        migrations.AddField(
            model_name = 'task',
            name = 'status',
            field = models.ForeignKey(null = True, on_delete = django.db.models.deletion.PROTECT, related_name = 'tasks', to = 'tasks.taskstatus'),
        ),
        migrations.AddField(
            model_name = 'task',
            name = 'priority',
            field = models.ForeignKey(null = True, on_delete = django.db.models.deletion.PROTECT, related_name = 'tasks', to = 'tasks.taskpriority'),
        ),
        migrations.RunPython(migrate_task_values_to_models, restore_task_values),
        migrations.RemoveField(
            model_name = 'task',
            name = 'status_legacy',
        ),
        migrations.RemoveField(
            model_name = 'task',
            name = 'priority_legacy',
        ),
        migrations.AlterField(
            model_name = 'task',
            name = 'status',
            field = models.ForeignKey(on_delete = django.db.models.deletion.PROTECT, related_name = 'tasks', to = 'tasks.taskstatus'),
        ),
        migrations.AlterField(
            model_name = 'task',
            name = 'priority',
            field = models.ForeignKey(on_delete = django.db.models.deletion.PROTECT, related_name = 'tasks', to = 'tasks.taskpriority'),
        ),
    ]
