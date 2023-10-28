from sshcheckers import ssh_checkout, upload_files
from yaml_reader import data


def deploy():
    res = []
    upload_files(
        data['host'],
        data['username'],
        data['password'],
        data['file_directory_path'],
        data['target_directory']
    )

    res.append(
        ssh_checkout(
            data['host'],
            data['username'],
            data['password'],
            "echo 'q1w2e3r4t5' | sudo -S dpkg -i /home/bam/p7zip-full.deb",
        )
    )

    res.append(
        ssh_checkout(
            data['host'],
            data['username'],
            data['password'],
            "echo 'q1w2e3r4t5' | sudo -S dpkg -s p7zip-full",
        )
    )

    return all(res)


if deploy():
    print("Успешно")
else:
    print("Ошибка")
