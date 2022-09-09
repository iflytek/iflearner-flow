#!/bin/bash

set -e

DEPLOY_HOME=$(cd `dirname $0`;pwd)

confirm(){
	echo -n "Please confirm that the component deployment is successful? yes/no: "
	while read confirm
	do
		case $confirm in
		yes | y | ye | Y )
			echo -e "\033[34mThe deployment is successful, Deployment continues\033[0m\n"
			sleep 1s
			break
			;;
		no | n | N )
			echo -e "\033[31mDeployment failed, please check\033[0m\n"
			exit 1
			;;
		*)
			echo -n "Input error, please enter again yes/no"
			;;
		esac
	done
}

uninstall_coms(){
	echo -n "Enter the uninstall Component? flow_server/mysql/pvc/all: "
	read COMP
	case $COMP in
	flow_server | flow | server | f )
		cd $DEPLOY_HOME/components/ && kubectl delete -f flow-server-srv.yaml
		;;
  mysql | mysq | my | m )
		cd $DEPLOY_HOME/components/ && kubectl delete -f flow-server-mysql.yaml
		;;
  pvc | p )
		cd $DEPLOY_HOME/components/ && kubectl delete -f flow-server-pvc.yaml
		;;
	all | a)
		echo "uninstall all flow Component"
		cd $DEPLOY_HOME/components/ && kubectl delete -f flow-server-srv.yaml
		sleep 1s
		cd $DEPLOY_HOME/components/ && kubectl delete -f flow-server-mysql.yaml
		sleep 1s
		cd $DEPLOY_HOME/components/ && kubectl delete -f flow-server-pvc.yaml
		sleep 1s
		;;
	*)
		echo "Component name error!!"
		return
		;;
	esac
}

init_sql(){
  service='flow-server-mysql'
  POD_ID=`kubectl get pods -n iflearner | grep $service | grep Running | awk '{print $1}' | tr -d "\n"`
  if [ -n "$POD_ID" ];then
    echo -e "\033[32;49;1mservice:  $service start success and is running------\033[0m\n"
    echo -e "\033[32;49;1mservice:  "$service" start import sql..........\033[0m\n"
    find $DEPLOY_HOME/components/sql/* | xargs -I{} kubectl cp {} iflearner/$POD_ID:/home/
#    kubectl cp $DEPLOY_HOME/components/sql/* $POD_ID:/home -n iflearner
    kubectl exec -it $POD_ID -n iflearner bash /home/load.sh
    echo -e "\033[32;49;1mservice:  "$service" import sql success------\033[0m\n"
  else
    echo -e "\033[31;49;1mservice $service not start!!!!!!!!!!!!!!\033[0m\n"
  fi
}

install_coms(){
	echo -n "Enter the install Component? pvc/mysql/flow_server/all: "
	read COMP
	case $COMP in
  pvc | p )
		cd $DEPLOY_HOME/components/ && kubectl apply -f flow-server-pvc.yaml
		;;
  mysql | mysq | my | m )
		cd $DEPLOY_HOME/components/ && kubectl apply -f flow-server-mysql.yaml
		sleep 10s
		init_sql
		;;
  flow_server | flow | server | f )
		cd $DEPLOY_HOME/components/ && kubectl apply -f flow-server-srv.yaml
		;;
	all | a)
		echo "install all flow Component"
		cd $DEPLOY_HOME/components/ && kubectl apply -f flow-server-pvc.yaml
		sleep 5s
		check_pvc flow-server-pvc
		confirm
		cd $DEPLOY_HOME/components/ && kubectl apply -f flow-server-mysql.yaml
		sleep 10s
		init_sql
		confirm
		cd $DEPLOY_HOME/components/ && kubectl apply -f flow-server-srv.yaml
		sleep 1s
		;;
	*)
		echo "Component name error!!"
		return
		;;
	esac
}

check_pod(){
    echo -e "###################status service##################\n"
    POD_ID=`kubectl get pods -n iflearner | grep $1 | grep Running | awk '{print $1}' | tr -d "\n"`
    if [ -n "$POD_ID" ]
    then
      echo -e "\033[32;49;1mservice:  "$1" startup successful and is running------\033[0m\n"
    else
      echo -e "\033[31;49;1mservice "$1" not started/running!\033[0m\n"
    fi
}

check_pvc(){
    echo -e "###################status pvc##################\n"
    pvc_name=`kubectl get pvc -n iflearner | grep $1 | grep Bound | awk '{print $1}' | tr -d "\n"`
    if [ -n "$pvc_name" ]
    then
      echo -e "\033[32;49;1mpvc:  "$1" Bound------\033[0m\n"
    else
      echo -e "\033[31;49;1mpvc "$1" not Bound!\033[0m\n"
    fi
}

status_coms(){
	echo -n "Enter the status Component? pvc/mysql/flow_server/all: "
	read COMP
	case $COMP in
  pvc | p )
		check_pvc flow-server-pvc
		;;
  mysql | mysq | my | m )
		check_pod flow-server-mysql
		;;
  flow_server | flow | server | f )
		check_pod flow-server-srv
		;;
	all | a)
		echo "status all flow Component"
		check_pvc flow-server-pvc
		check_pod flow-server-mysql
		check_pod flow-server-srv
		;;
	*)
		echo "Component name error!!"
		return
		;;
	esac
}

function help(){
 	echo -e "Usage: flow server deploy.sh [OPTIONS]
    Options:
    \t\033[32;49;1minstall\033[0m         -i               install    flow all compenont service
    \t\033[32;49;1mstatus\033[0m          -s             status     flow all compenont service
    \t\033[32;49;1muninstall\033[0m       -u               uninstall  flow all compenont service
    \t\033[32;49;1mhelp\033[0m            -h               print usage \n"
	exit
}

if [ -z "$1" ]; then
	help
fi

case "$1" in
	-i|install)
		install_coms
		;;
	-s|status)
		status_coms
		;;
	-u|uninstall)
		uninstall_coms
		;;
	*)
		help
		;;
esac

exit

