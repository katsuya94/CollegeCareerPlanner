# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TermPlan'
        db.create_table(u'plan_termplan', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('term', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'plan', ['TermPlan'])

        # Adding M2M table for field taking on 'TermPlan'
        m2m_table_name = db.shorten_name(u'plan_termplan_taking')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('termplan', models.ForeignKey(orm[u'plan.termplan'], null=False)),
            ('offering', models.ForeignKey(orm[u'kb.offering'], null=False))
        ))
        db.create_unique(m2m_table_name, ['termplan_id', 'offering_id'])

        # Adding model 'Plan'
        db.create_table(u'plan_plan', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('grad_year', self.gf('django.db.models.fields.IntegerField')()),
            ('grad_term', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'plan', ['Plan'])

        # Adding M2M table for field reqs on 'Plan'
        m2m_table_name = db.shorten_name(u'plan_plan_reqs')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('plan', models.ForeignKey(orm[u'plan.plan'], null=False)),
            ('course', models.ForeignKey(orm[u'kb.course'], null=False))
        ))
        db.create_unique(m2m_table_name, ['plan_id', 'course_id'])

        # Adding M2M table for field term_plans on 'Plan'
        m2m_table_name = db.shorten_name(u'plan_plan_term_plans')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('plan', models.ForeignKey(orm[u'plan.plan'], null=False)),
            ('termplan', models.ForeignKey(orm[u'plan.termplan'], null=False))
        ))
        db.create_unique(m2m_table_name, ['plan_id', 'termplan_id'])


    def backwards(self, orm):
        # Deleting model 'TermPlan'
        db.delete_table(u'plan_termplan')

        # Removing M2M table for field taking on 'TermPlan'
        db.delete_table(db.shorten_name(u'plan_termplan_taking'))

        # Deleting model 'Plan'
        db.delete_table(u'plan_plan')

        # Removing M2M table for field reqs on 'Plan'
        db.delete_table(db.shorten_name(u'plan_plan_reqs'))

        # Removing M2M table for field term_plans on 'Plan'
        db.delete_table(db.shorten_name(u'plan_plan_term_plans'))


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
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
        },
        u'plan.plan': {
            'Meta': {'object_name': 'Plan'},
            'grad_term': ('django.db.models.fields.IntegerField', [], {}),
            'grad_year': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reqs': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['kb.Course']", 'symmetrical': 'False'}),
            'term_plans': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['plan.TermPlan']", 'symmetrical': 'False'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'plan.termplan': {
            'Meta': {'object_name': 'TermPlan'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'taking': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['kb.Offering']", 'symmetrical': 'False'}),
            'term': ('django.db.models.fields.IntegerField', [], {}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['plan']