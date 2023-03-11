WHATEVER := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
$(eval $(WHATEVER):;@:)
# ^ Captures all the stuff passed after the target. If you are going
# to pass options, you may do so by using "--" e.g.:
# make up -- --build

project = sahan
cc = docker compose -p $(project) -f docker-compose.yml
ex = docker exec -it sahan-web
dj = $(ex) python manage.py

.PHONY: *

build:
	$(cc) build $(WHATEVER)
up:
	$(cc) up $(WHATEVER)
down:
	$(cc) down $(WHATEVER)
compose:
	$(cc) $(WHATEVER)
logs:
	docker logs $(WHATEVER) --tail 500 --follow
console:
	$(ex) /bin/sh
run:
	$(dj) $(WHATEVER)
shell:
	$(dj) shell
