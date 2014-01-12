# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Offering.instructor'
        db.add_column(u'kb_offering', 'instructor',
                      self.gf('django.db.models.fields.CharField')(default='mr. man', max_length=200),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Offering.instructor'
        db.delete_column(u'kb_offering', 'instructor')


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
            'instructor': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
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