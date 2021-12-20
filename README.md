# task1
1. Add host ssh key to your ssh client 
    * `eval $(ssh-agent -s)`
    * `ssh-add ~/.ssh/id_rsa`
2. Run playbook `ansible-playbook -i inventory.yml playbook.yml`
# task2
1. Run `docker build -t modestas/letsimaginewehaverepo .`
2. Run `docker push modestas/letsimaginewehaverepo`