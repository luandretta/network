// Toggle to reply a comment
function commentReplyToggle(parent_id) {
    const row = document.getElementById('parent_id');

    if (row.classList.contains('d-none')){
        row.classList.remove('d-none');
    } else {
        row.classList.add('d-none');
    }
}

// Toggle to show notifications
function showNotifications() {
    const container = document.getElementById('notification-container');

    if (container.classList.contains('d-none')){
        container.classList.remove('d-none');
    } else {
        container.classList.add('d-none');
    }
}
