#### Test Django Critial Functionalities

environment
tdb
Freenome free domain name
nepexgroup.tk 
80.80.80.80
80.80.81.81

#### Procedure
* with fresh database
* migrate_shcemas
* create tenant in public schema (for website pricing, registration form)
* create another tenant that `ORGANIZATION_ADMIN` used to manage all public model or apps
```
Client.objects.create(domain_url='nepexgroup.tk', schema_name='public', name='nepex website')
Client.objects.create(domain_url='nepex.nepexgroup.tk', schema_name='nepex', name='nepex tenant')
Client.objects.create(domain_url='client.nepexgroup.tk', schema_name='client1', name='client1 tenant')
```
#### Docker Procedure
```
# Build docker image
docker build .
# migrate django application
docker-compose run web python /code/manage.py migrate_schemas --noinput
# create superuser
docker-compose run web python /code/manage.py createsuperuser
# Build container and run
docker-compose up -d --build
# Disable container
docker-compose down
```
#### Endpoint
`/admin/` for all tenant admin
`/nepex/tenant-admin/` for ORGANIZATION_ADMIN but faced public

#### Frontend
[https://github.com/vimm0/test-django-frontend](https://github.com/vimm0/test-django-frontend)
