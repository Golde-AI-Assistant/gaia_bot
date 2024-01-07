import asyncio
import json
import webbrowser

from gaia_bot.skills.assistant_skill import AssistantSkill
from gaia_bot.configs.port_configs import PORTS, DOMAIN
from gaia_bot.utils.activate_microservice import check_microservice_state_by_name, check_port_in_use


class OpenClientGUI(AssistantSkill):
    
    @classmethod
    async def open_client_gui(cls, text, **kwargs):
        if check_microservice_state_by_name('client_gui') == False:
            print("Client GUI is running...")
            await cls._activate_client_gui()
        await cls._open_browser()    
    # def __init__(self): 
    #     self.client_gui = "client_gui"

    # async def open_client_gui(self):
    #     await self._open_browser()

    async def _open_browser():
        port = PORTS['client_gui']['port']
        url = f"http://{DOMAIN}:{port}/"
        return await webbrowser.open(url)
     
    async def _activate_client_gui():
        bash_script_path = PORTS['client_gui']['shell_path']
        await asyncio.create_subprocess_exec('gnome-terminal', '--', 'bash', '-c', f'bash {bash_script_path}')

    # # async def _connect_client_gui(self, access_token, refresh_token):
    # #     client_gui_command = ClientGUICommand(access_token, refresh_token)
    # #     await client_gui_command.connect_client_gui_command()
    # #     # TODO

    # async def _wait_client_gui(self):
    #     while True:
    #         client_gui_ready = check_port_in_use(PORTS[self.client_gui]['port'])
    #         if client_gui_ready:
    #             return True
    #         await asyncio.sleep(1)
        
    # def _get_token_parameters(self):
    #     filepath = "..\\..\\local\\resources\\authen_cache\\response.json"
    #     with open(filepath, "r") as f:
    #         response = json.load(f)
    #     return response['accessToken'], response['refreshToken']