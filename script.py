
from github import GitHub
# curl -u 'georgekun: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' https://api.github.com/user/repos -d '{"name":"explorer_flask"}'




def manager_commnad(command:int):
	hub = GitHub()	
 
	match command:
		case 0:
			return False
		case 1:
			hub.create_repo()
			
		case 2:
			hub.delete_repo()
   
		case 3:
			hub.auth()
		case _:
			return 
			
	return True


def main(): 
	while True:
		print("""
Commands:
close script - 0
create repository - 1
delete repository - 2
save auth - 3
			""")
		command = int(input("Выберите command: "))
		if manager_commnad(command):
			continue
		else:
			break
		
		
	

if __name__ == "__main__":
	main()