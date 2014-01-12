# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Department'
        db.create_table(u'kb_department', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'kb', ['Department'])

        # Adding model 'Course'
        db.create_table(u'kb_course', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('dept', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['kb.Department'])),
            ('num', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'kb', ['Course'])

        # Adding model 'Times'
        db.create_table(u'kb_times', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('mon', self.gf('django.db.models.fields.IntegerField')()),
            ('tue', self.gf('django.db.models.fields.IntegerField')()),
            ('wed', self.gf('django.db.models.fields.IntegerField')()),
            ('thu', self.gf('django.db.models.fields.IntegerField')()),
            ('fri', self.gf('django.db.models.fields.IntegerField')()),
            ('duration', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'kb', ['Times'])

        # Adding model 'Offering'
        db.create_table(u'kb_offering', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['kb.Course'])),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('term', self.gf('django.db.models.fields.IntegerField')()),
            ('times', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['kb.Times'], unique=True)),
        ))
        db.send_create_signal(u'kb', ['Offering'])


    def backwards(self, orm):
        # Deleting model 'Department'
        db.delete_table(u'kb_department')

        # Deleting model 'Course'
        db.delete_table(u'kb_course')

        # Deleting model 'Times'
        db.delete_table(u'kb_times')

        # Deleting model 'Offering'
        db.delete_table(u'kb_offering')


    models = {
        u'kb.course': {
            'Meta': {'object_name': 'Course'},
            'dept': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['kb.Department']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'kb.department': {
            'Meta': {'object_name': 'Department'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'kb.offering': {
            'Meta': {'object_name': 'Offering'},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['kb.Course']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'term': ('django.db.models.fields.IntegerField', [], {}),
            'times': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['kb.Times']", 'unique': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        u'kb.times': {
            'Meta': {'object_name': 'Times'},
            'duration': ('django.db.models.fields.IntegerField', [], {}),
            'fri': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mon': ('django.db.models.fields.IntegerField', [], {}),
            'thu': ('django.db.models.fields.IntegerField', [], {}),
            'tue': ('django.db.models.fields.IntegerField', [], {}),
            'wed': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['kb']