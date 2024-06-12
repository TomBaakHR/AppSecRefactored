import sys

from Configuration.DatabaseConfiguration import DatabaseConfiguration
from Configuration.DatabaseSeeder import DatabaseSeeder
from Controllers.LoginController import LoginController
from Controllers.MemberController import MemberController
from Debug.ConsoleLogger import ConsoleLogger
from Enum.Color import Color
from Repository.MemberRepository import MemberRepository
from Service.EncryptionService import EncryptionService
from Service.IndexService import IndexService
from Test.CreateAdminTest import CreateAdminTest
from Test.CreateMemberTest import CreateMemberTest
from View.UserInterfaceAlert import UserInterfaceAlert
from View.UserInterfaceFlow import UserInterfaceFlow


def main():

    UserInterfaceFlow.quick_run(UserInterfaceAlert("-= Welkom in het User Management systeem van Unique Meal =-", Color.HEADER), 1)

    UserInterfaceFlow.quick_run(UserInterfaceAlert("[ ] Keys initialiseren..."), 0)

    EncryptionService.create_certificates_if_not_exist()

    UserInterfaceFlow.quick_run(UserInterfaceAlert("[+] Keys geïnitialiseerd", Color.OKGREEN), 0)

    UserInterfaceFlow.quick_run(UserInterfaceAlert("[ ] Database initialiseren..."), 0)

    DatabaseConfiguration.start()
    DatabaseSeeder.seed()

    UserInterfaceFlow.quick_run(UserInterfaceAlert("[+] Database geïnitialiseerd ", Color.OKGREEN), 0)

    UserInterfaceFlow.quick_run(UserInterfaceAlert("[ ] Database indexeren..."), 0)

    IndexService.index_database()

    UserInterfaceFlow.quick_run(UserInterfaceAlert("[+] Database geïndexeerd ", Color.OKGREEN), 0)

    # CreateMemberTest.run()
    # CreateAdminTest.run(uname="admin", pword="admin")
    # exit(0)

    lc = LoginController()
    lc.login()


if __name__ == '__main__':

    # DEBUG CONSOLE LOGGING
    if len(sys.argv) > 1:
        match sys.argv[1].lower():
            case "-v":
                ConsoleLogger.set_loglevel(1)
            case "-vv":
                ConsoleLogger.set_loglevel(2)
            case "-vvv":
                ConsoleLogger.set_loglevel(3)

    main()
