from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('liveclasses', '0003_alter_liveclass_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name = 'liveclass',
            name = 'meeting_link',
        ),
    ]
