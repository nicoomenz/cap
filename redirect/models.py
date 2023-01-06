from django.db import models

# Create your models here.
class  TmobAudit(models.Model):
    _created_at = models.DateTimeField(auto_now_add=True)
    _update_at = models.DateTimeField(auto_now=True)
    class Meta:
       abstract = True
        
    @property
    def created_at(self):
        return self.created_at

    @property
    def update_at(self):
        return self.updated_at

    
class Redirect(TmobAudit):
    
    _key=models.CharField(max_length=36, db_index=True)
    _url=models.CharField(max_length=50)
    _active= models.BooleanField(default=True)
    
    @property
    def key(self):
        return self._key

    @property
    def url(self):
        return self._url
        
    @property
    def active(self):    
        return self._active

    @key.setter
    def key(self, value):
        self._key = value
        
    @url.setter
    def url(self, value):
        self._url = value

    @active.setter
    def active(self, value):
        self._active = value

       
    def get_redirect(self):
        return self.url
    @classmethod
    def create(cls, key, url, active=True):
        return cls.objects.create(_key=key,_url=url,_active=active)
        


class HistoricalRedirect(TmobAudit):
    NF="NOT FOUND"
    CACHE="CACHE"
    DB="DB"
   
    STATUS = (
        (NF, "Not Found"),
        (CACHE, "Cache"),
        (DB, "Data Base"),
        )

    found = models.BooleanField(default=False)
    status = models.CharField(max_length=10,choices= STATUS, default=NF)
    key = models.CharField(max_length=36)
    url = models.CharField(max_length=50,null=True,blank=True)

    @classmethod
    def create(cls,key,url,status):
        if url:
            return cls.objects.create(key=key,url=url,status=status,found=True)
        return cls.objects.create(key=key,url=url,status=status,found=False)