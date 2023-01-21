from django.test import SimpleTestCase, Client
from django.urls import reverse

from .utils.fuzzy_matching import levenshtein_distance
from .utils.helper import calculate_matching_percentage


class TextMatchTests(SimpleTestCase):
    def test_levenshtein_distance(self):
        s1 = 'ALCURONIUM CHLORIDE 5MG/ML 2ML INJECTION'
        s2 = 'ABACAVIR SULFATE 300MG TABLET'
        distance = levenshtein_distance(s1, s2)
        self.assertEqual(distance, 30)
            
    def test_matching_percentage(self):
        s1 = 'ALCURONIUM CHLORIDE 5MG/ML 2ML INJECTION'
        s2 = 'ABACAVIR SULFATE 300MG TABLET'
        percentage = calculate_matching_percentage(s1, s2)
        self.assertEqual(percentage, -3.4482758620689653)
    
    def test_get_keys(self):
        client = Client()
        response = client.get(reverse('list-keys'))
        self.assertEqual(response.status_code, 200)
        
    def test_get_values_not_found(self):
        client = Client()
        response = client.post(reverse('get-values'), data={'key':'SUXfas3c de3c 3 ON'})
        self.assertEqual(response.status_code, 404)
    
    def test_get_values_found(self):
        client = Client()
        response = client.post(reverse('get-values'), data={'key':'SUXAMETHONIUM 500MG INJECTION'})
        self.assertEqual(response.status_code, 200)
