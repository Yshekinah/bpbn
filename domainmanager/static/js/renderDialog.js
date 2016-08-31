function displayNote(text) {
    BootstrapDialog.show({
        message: text,
        buttons: [{
            label: 'Ok',
            cssClass: 'btn-primary',
            action: function (dialogItself) {
                dialogItself.close();
            }
        }]
    });
}