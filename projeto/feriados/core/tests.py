from django.test import TestCase

class NatalTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')

    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)

    def test_texto(self):
        self.assertContains(self.resp, 'natal')
    
    def test_template_natal(self):
        self.assertTemplateUsed(self.resp, 'natal.html')
 
        
class TiradentesTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/tiradentes')
    
    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)
    
    def test_texto(self):
        self.assertContains(self.resp, 'tiradentes')

    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'tiradentes.html')


from core.models import FeriadoModel
from datetime import datetime
class FeriadoModelTest(TestCase):
    def setUp(self):
        self.feriado = 'Natal'
        self.mes = 12
        self.dia = 25
        self.cadastro = FeriadoModel(
            nome=self.feriado, 
            dia=self.dia, 
            mes=self.mes,
        )
        self.cadastro.save()

    def test_created(self):
        self.assertTrue(FeriadoModel.objects.exists())

    def test_modificado_em(self):
        self.assertIsInstance(self.cadastro.modificado_em, datetime)

    def test_nome_feriado(self):
        nome = self.cadastro.__dict__.get('nome', '')
        self.assertEqual(nome, self.feriado)

    def test_dia_feriado(self):
        dia = self.cadastro.__dict__.get('dia', '')
        self.assertEqual(dia, self.dia)

from core.forms import FeriadoForm, FeriadoModelForm

class FormFeriadoTest(TestCase):
    def test_form_has_fields(self):
        form = FeriadoForm()
        expected = ['nome', 'dia', 'mes']
        self.assertSequenceEqual(expected, list(form.fields))
    
    def test_must_be_capitalized(self):
        form = self.make_validated_form(nome='dia de são nunca')
        self.assertEqual('DIA DE SÃO NUNCA', form.cleaned_data['nome'])
    
    def test_must_be_capitalized2(self):
        form = self.make_validated_form()
        self.assertEqual('TIRADENTES', form.cleaned_data['nome'])

     
    def make_validated_form(self, **kwargs):
        valid = dict(
        nome='Tiradentes',
        dia=14, 
        mes=4
        )
        data = dict(valid, **kwargs)
        form = FeriadoForm(data)
        form.is_valid()
        return form


class FeriadoModelFormTest(TestCase):
    def test_form_has_fields(self):
        form = FeriadoModelForm()
        expected = ['nome', 'dia', 'mes']
        self.assertSequenceEqual(expected, list(form.fields))
    
    def test_must_be_capitalized(self):
        form = self.make_validated_form(nome='dia de são nunca')
        self.assertEqual('DIA DE SÃO NUNCA', form.cleaned_data['nome'])
    
    def test_must_be_capitalized2(self):
        form = self.make_validated_form()
        self.assertEqual('TIRADENTES', form.cleaned_data['nome'])

     
    def make_validated_form(self, **kwargs):
        valid = dict(
        nome='Tiradentes',
        dia=14, 
        mes=4
        )
        data = dict(valid, **kwargs)
        form = FeriadoModelForm(data)
        form.is_valid()
        return form