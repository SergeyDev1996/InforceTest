from django.db import models, IntegrityError


class Menu(models.Model):
    menu_items = models.TextField()


class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    votes = models.IntegerField(default=0)
    menu_monday = models.TextField(blank=True, default='Menu was not published yet')
    menu_tuesday = models.TextField(blank=True, default='Menu was not published yet')
    menu_wednesday = models.TextField(blank=True, default='Menu was not published yet')
    menu_thursday = models.TextField(blank=True, default='Menu was not published yet')
    menu_friday = models.TextField(blank=True, default='Menu was not published yet')
    menu_saturday = models.TextField(blank=True, default='Menu was not published yet')
    menu_sunday = models.TextField(blank=True, default='Menu was not published yet')


class Vote(models.Model):
    restaurant = models.ForeignKey(
        to=Restaurant,
        on_delete=models.CASCADE,
        related_name='vote'
    )

    def save(self, commit=True, *args, **kwargs):
        if commit:
            try:
                self.restaurant.votes += 1
                self.restaurant.save()
                super(Vote, self).save(*args, **kwargs)

            except IntegrityError:
                self.restaurant.votes -= 1
                self.restaurant.save()
                raise IntegrityError
        else:
            raise IntegrityError

