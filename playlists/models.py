from django.db import models
from tracks.models import Tracks

from users.models import User


# class CartQueryset(models.QuerySet):
#
#     def total_price(self):
#         return sum(cart.products_price() for cart in self)
#
#     def total_quantity(self):
#         if self:
#             return sum(cart.quantity for cart in self)
#         return 0


class Playlist(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Пользователь')
    track = models.ForeignKey(to=Tracks, on_delete=models.CASCADE, verbose_name='Трек')
    session_key = models.CharField(max_length=32, null=True, blank=True)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        db_table = 'playlist'
        verbose_name = "Плейлист"
        verbose_name_plural = "Плейлист"

    # objects = CartQueryset().as_manager()


    def __str__(self):
        if self.user:
            return f'Плейлист {self.user.username} | Трек {self.track.title}'

        return f'Анонимный плейлист | Трек {self.track.title}'