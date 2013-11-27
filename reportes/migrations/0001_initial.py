# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Materia'
        db.create_table(u'reportes_materia', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'reportes', ['Materia'])

        # Adding model 'Alumno'
        db.create_table(u'reportes_alumno', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('archivo', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'reportes', ['Alumno'])

        # Adding M2M table for field materia on 'Alumno'
        m2m_table_name = db.shorten_name(u'reportes_alumno_materia')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('alumno', models.ForeignKey(orm[u'reportes.alumno'], null=False)),
            ('materia', models.ForeignKey(orm[u'reportes.materia'], null=False))
        ))
        db.create_unique(m2m_table_name, ['alumno_id', 'materia_id'])


    def backwards(self, orm):
        # Deleting model 'Materia'
        db.delete_table(u'reportes_materia')

        # Deleting model 'Alumno'
        db.delete_table(u'reportes_alumno')

        # Removing M2M table for field materia on 'Alumno'
        db.delete_table(db.shorten_name(u'reportes_alumno_materia'))


    models = {
        u'reportes.alumno': {
            'Meta': {'object_name': 'Alumno'},
            'archivo': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'materia': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['reportes.Materia']", 'symmetrical': 'False'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'reportes.materia': {
            'Meta': {'object_name': 'Materia'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['reportes']