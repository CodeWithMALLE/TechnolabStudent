from django.db import models
from accounts.models import Users
from django.core.validators import RegexValidator


# Create your models here.


class Filiere(models.Model):
	nom = models.CharField(max_length=200)


class Cycle(models.Model):
	nom = models.CharField(max_length=200)
	nb_niveau = models.IntegerField(
		validators=[RegexValidator(regex=r'^(\d){1,3}$', message="Valeur non valide !")])

	def __str__(self):
		return self.nom


class Niveau(models.Model):
	cycle = models.ForeignKey(Cycle, on_delete=models.CASCADE)
	programme = models.FileField(blank=True)


class Frais(models.Model):
	filiere = models.ForeignKey(Filiere, on_delete=models.SET_NULL, null=True)
	cycle = models.ForeignKey(Cycle, on_delete=models.CASCADE)
	niveau = models.ForeignKey(Niveau, on_delete=models.CASCADE)
	montant = models.IntegerField(blank=True)


class Etudiant(Users):
	matricule = models.CharField(
		max_length=200, unique=True, blank=False, null=False,
		unique_for_year=True
		)
	nom = models.CharField(max_length=200)
	prenom = models.CharField(max_length=200)

	dir_files = "students_files/" + str(prenom) + "_" + str(nom) + "/"
	acte_naissance = models.FileField(
		upload_to=dir_files, verbose_name="Votre acte de  naissance"
	)
	attestation_bac = models.FileField(upload_to="students_files/")
	cycle = models.ForeignKey(Cycle, on_delete=models.CASCADE)
	filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE)
	niveau = models.ForeignKey(Niveau, on_delete=models.CASCADE)
	frais = models.ForeignKey(Frais, on_delete=models.SET_DEFAULT, default=0, blank=True)

	class Meta:
		verbose_name = "Etudiant"
		verbose_name_plural = "Etudiants"
