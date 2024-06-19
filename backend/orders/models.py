from django.db import models
import uuid

class Order(models.Model):
    customer = models.ForeignKey('customers.Customer', on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    order_number = models.CharField(max_length=200,null=True, blank=True)
    quantity = models.PositiveIntegerField(default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    status = models.CharField(max_length=200, default='Pending', choices=(('Pending', 'Pending'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled')))
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
    
    @property
    def get_total(self):
        return self.quantity * self.product.price
    
    @property
    def get_total_price(self):
        return self.total_price
    
    @property
    def get_total_quantity(self):
        return self.quantity

    def generate_order_number(self):
        return 'ORD-' + str(uuid.uuid4()).split('-')[-1].upper()
    
    def save(self, *args, **kwargs):
        if self.order_number == '':
            self.order_number = self.generate_order_number()
        if self.total_price == 0:
            self.total_price = self.get_total
        super().save(*args, **kwargs)


    def __str__(self):
        return self.customer.name + ' - ' + self.product.name