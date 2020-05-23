import states_and_files as sf
import os
import user_interface as ui


if __name__ == '__main__':
	interact = input('Run interactively (y/n)?\n')
	if interact == 'y':
		project_root = ui.get_project_root()
		juris_name = None

	else:
		d = ui.config(section='050',msg='Pick a paramfile for testing.')
		project_root = d['project_root']
		juris_name = d['juris_name']

	j_path = os.path.join(project_root,'jurisdictions')

	juris = ui.pick_juris_from_filesystem(project_root,j_path,check_files=True,juris_name=juris_name)

	print(f'Context files for {juris.short_name} are internally consistent.')
	exit()
