# -*- mode: ruby -*-
# vi: set ft=ruby :
# vi: set ts=2 sw=2 expandtabs :

Vagrant.configure("2") do |config|
  config.vm.box = "trusty64"
  config.vm.box_url = "http://cloud-images.ubuntu.com/vagrant/trusty/current/trusty-server-cloudimg-amd64-vagrant-disk1.box"

  config.vm.network :forwarded_port, guest: 8000, host: 8000

  config.vm.synced_folder ".", "/home/vagrant/code"

  # Only used for vendoring puppet modules
  config.librarian_puppet.puppetfile_dir = "puppet"  
  config.librarian_puppet.placeholder_filename = ".gitignore"
  
  config.vm.provision :puppet do |puppet|
    puppet.manifests_path = "puppet/manifests"
    puppet.manifest_file  = "vagrant.pp"
    puppet.module_path = ["puppet/modules", "puppet/localmodules"]
  end

  config.vm.provider :virtualbox do |vb|
    vb.customize ["modifyvm", :id, "--memory", "2048"]
  end

end
