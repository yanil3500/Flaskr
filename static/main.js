$(() => console.log('ready!')); // sanity check

$('.entry').on('click', () => {
  const entry = this
  const postId = $(this).find('h2').attr('id')
  $.ajax({
    type: 'GET',
    url: `/delete/${postId}`,
    context: entry,
    success: (result) => {
      if (result.status == 1) {
        $(this).remove();
        console.log('result :', result);
      }
    }
  });
});

