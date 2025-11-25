function eliminarPerfume(id) {
  if (!confirm('¿Seguro que quieres eliminar este perfume?')) return

  fetch(`/api/perfumes/${id}/`, {
    method: 'DELETE',
    // headers: {
    //   'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzYwNDc5MTE5LCJpYXQiOjE3NjA0Nzg4MTksImp0aSI6ImQzZjEwNWNkNWVhODQ2Y2JhYzA1MmZhMDBhODBiNTI3IiwidXNlcl9pZCI6IjIifQ.g0_ucCShyTuuqc15lhHFbpNEI-SWOxtK8xRJxJs342k',
    //   'Content-Type': 'application/json'
    // }
  })
    .then(res => {
      if (res.status === 204) {
        alert('Perfume eliminado')
        location.reload()
      } else {
        return res.json().then(data => {
          alert(data.detail || 'No se pudo eliminar el perfume')
        })
      }
    })
    .catch(() => alert('A ocurrido un error'))
}