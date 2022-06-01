from django.db import models

# Create your models here.

class Player(models.Model):
    discordId = models.CharField(max_length=200, unique=True)
    
    def __str__(self):
         return self.discordId
        
class Game(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date scheduled')
    image = models.ImageField(upload_to = 'images/', blank=True)
    host = models.CharField(max_length=100)
    player = models.ManyToManyField(Player, blank=True)
    played = models.BooleanField(default=False)
    
    def __str__(self):
        return "%s, %s"%(self.name, self.pub_date.strftime("%d/%b/%Y, %I:%M%p"))
    
class Winners(models.Model):
    position = models.PositiveIntegerField()
    game= models.ForeignKey(Game, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    
    def __str__(self):
        return "%s, %s, %d"%(self.player.discordId, self.game.name, self.position)

    class Meta:
           unique_together = ("game", "position")
    
        