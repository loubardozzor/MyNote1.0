from django.db import models

# Create your models here.

# Create your models here.
"""dati sugli Studenti"""
class Studente(models.Model):
    nome=models.CharField(max_length=100)
    cognome=models.CharField(max_length=100)
    dataNascita=models.DateField(null=True, blank=True)
    Username = models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    email = models.EmailField(max_length=100)
    def __str__(self):
        return f"{self.nome} {self.cognome} {self.dataNascita}"
    #class Meta:




"""dati sulle Materie della Laurea triennale in ingegneria
ingegneria informatica"""

class Materia(models.Model):
    nome=models.CharField(max_length=100)
    codMat=models.CharField(max_length=100)
    def __str__(self):
        return f"{self.nome} {self.codMat}"




class Appunto(models.Model):
    nome_appunto = models.CharField(max_length=100, null=True, blank=True)
    pdf_appunto = models.FileField(upload_to='pdfs/', null=True, blank=True)
    voto_medio = models.IntegerField(null=True, blank=True)  #attributo derivato
    Num_scaricamento = models.IntegerField() #attributo derivato
    studente = models.ForeignKey(Studente, null=True, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, null=True, on_delete=models.SET_NULL)
    data_caricamento = models.DateTimeField()
    def __str__(self):
        #return f"{self.nome_appunto} {self.studente.nome} {self.materia}"
        pass
    class Meta:
        unique_together = ['nome_appunto',  'pdf_appunto']



"""dati sullo scaricamento degli Appunti"""
class Scarica(models.Model):
    studente=models.ForeignKey(Studente, null=True, on_delete=models.SET_NULL)
    appunto_scaricato=models.ForeignKey(Appunto, null=True, on_delete=models.SET_NULL)
    data_scaricamento=models.DateTimeField()
    voto_assegnato=models.IntegerField(null=True, blank=True)
    def __str__(self):
        return f"{self.studente.nome} {self.data_scaricamento} {self.voto_assegnato}"
    class Meta:
        unique_together = ['studente', 'appunto_scaricato','data_scaricamento']

""" dati sulla recenzione di un appunto da uno studente"""
class Recenzione(models.Model):
    studente=models.ForeignKey(Studente,null=True, on_delete=models.SET_NULL)
    appunto_recenzionato=models.ForeignKey(Appunto, null=True, on_delete=models.SET_NULL)
    data_recenzione= models.DateTimeField()
    testo_recenzione= models.CharField(max_length=200)
    def __str__(self):
        return f"{self.studente.nome} {self.data_recenzione} {self.testo_recenzione}"

    class Meta:
        unique_together = ['studente', 'appunto_recenzionato', 'data_recenzione']


""" dati sulla cancellazione degli Appunti da uno studente """
class Cancella(models.Model):
    appunto=models.ForeignKey(Appunto, null=True, on_delete=models.SET_NULL)
    studente= models.ForeignKey(Studente, null=True, on_delete=models.SET_NULL)
    data_cancellazione=models.DateTimeField()
    def __str__(self):
        return f"{self.appunto.docpdf.nome} {self.studente.nome} {self.data_cancellazione}"



