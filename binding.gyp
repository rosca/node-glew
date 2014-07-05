{
  'targets' : [
    {
      'target_name' : 'glew-static',
      'type' : 'static_library',
      'sources' : [
        'deps/glew/src/glew.c'
      ],
      'include_dirs' : [
        'deps/glew/include'
      ]
    }
  ]
}
